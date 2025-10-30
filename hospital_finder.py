import json
from typing import List, Dict, Tuple, Optional
from geopy.distance import geodesic
import geocoder


class HospitalFinder:
    """Rule-based hospital finder with location detection and filtering"""
    
    def __init__(self):
        self.hospitals_data = self.load_hospitals()
        self.hospitals = self.hospitals_data.get('hospitals', [])
        self.disease_mapping = self.hospitals_data.get('diseaseSpecializationMapping', {})
    
    def load_hospitals(self) -> Dict:
        """Load hospital data from JSON"""
        try:
            with open('hospitals.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "hospitals": [],
                "diseaseSpecializationMapping": {}
            }
    
    def get_user_location(self) -> Optional[Tuple[float, float, str]]:
        """
        Get user's current location using IP-based geolocation
        Returns (lat, lon, city) or None
        """
        try:
            g = geocoder.ip('me')
            if g.ok:
                return (g.latlng[0], g.latlng[1], g.city if g.city else "Unknown")
        except Exception as e:
            print(f"Location detection error: {e}")
        return None
    
    def get_specializations_for_disease(self, disease_name: str) -> List[str]:
        """Get relevant medical specializations for a disease"""
        return self.disease_mapping.get(disease_name, ["General Medicine"])
    
    def calculate_distance(self, user_coords: Tuple[float, float], 
                          hospital_coords: Tuple[float, float]) -> float:
        """
        Calculate distance between user and hospital in kilometers
        """
        try:
            return geodesic(user_coords, hospital_coords).kilometers
        except Exception as e:
            print(f"Distance calculation error: {e}")
            return float('inf')
    
    def calculate_travel_time(self, distance_km: float, avg_speed_kmh: float = 30.0) -> str:
        """
        Calculate estimated travel time based on distance
        Uses average city traffic speed of 30 km/h by default
        Returns formatted time string (e.g., "15 mins", "1 hr 20 mins")
        """
        if distance_km is None or distance_km == float('inf'):
            return "N/A"
        
        time_hours = distance_km / avg_speed_kmh
        time_minutes = time_hours * 60
        
        if time_minutes < 60:
            return f"{int(time_minutes)} mins"
        else:
            hours = int(time_minutes // 60)
            minutes = int(time_minutes % 60)
            if minutes > 0:
                return f"{hours} hr {minutes} mins"
            else:
                return f"{hours} hr"
    
    def filter_hospitals_by_city(self, city: str) -> List[Dict]:
        """Filter hospitals by city name"""
        if not city:
            return self.hospitals
        
        city_lower = city.lower().strip()
        filtered = []
        
        for hospital in self.hospitals:
            if hospital.get('city', '').lower() == city_lower:
                filtered.append(hospital)
        
        return filtered if filtered else self.hospitals
    
    def filter_hospitals_by_specialization(self, hospitals: List[Dict], 
                                          specializations: List[str]) -> List[Dict]:
        """
        Filter hospitals that have matching specializations
        """
        if not specializations:
            return hospitals
        
        filtered = []
        spec_lower = [s.lower() for s in specializations]
        
        for hospital in hospitals:
            hospital_specs = [s.lower() for s in hospital.get('specializations', [])]
            if any(spec in hospital_specs for spec in spec_lower):
                filtered.append(hospital)
        
        return filtered if filtered else hospitals
    
    def find_nearby_hospitals(self, 
                            disease_name: str, 
                            user_coords: Optional[Tuple[float, float]] = None,
                            city: Optional[str] = None,
                            max_distance: float = 50.0,
                            sort_by: str = "distance") -> List[Dict]:
        """
        Main function to find nearby hospitals for a disease
        
        Args:
            disease_name: Detected disease name
            user_coords: (lat, lon) tuple or None for automatic detection
            city: City name for filtering
            max_distance: Maximum distance in km (only applied if city matches user's city)
            sort_by: 'distance' or 'rating'
        
        Returns:
            List of hospitals with distance info
        """
        required_specs = self.get_specializations_for_disease(disease_name)
        
        # Determine if we should apply distance filtering
        # Only filter by distance if no specific city is selected or if all hospitals are close enough
        apply_distance_filter = False
        if city:
            hospitals = self.filter_hospitals_by_city(city)
        else:
            hospitals = self.hospitals.copy()
            apply_distance_filter = True  # Apply distance filter for nearby search
        
        hospitals = self.filter_hospitals_by_specialization(hospitals, required_specs)
        
        results = []
        for hospital in hospitals:
            hospital_coords = (hospital.get('lat'), hospital.get('lon'))
            
            result = hospital.copy()
            
            if user_coords and hospital_coords[0] and hospital_coords[1]:
                distance = self.calculate_distance(user_coords, hospital_coords)
                result['distance_km'] = round(distance, 2)
                result['travel_time'] = self.calculate_travel_time(distance)
                
                # Only filter by distance if we're doing a nearby search (no specific city selected)
                if apply_distance_filter and distance > max_distance:
                    continue
            else:
                result['distance_km'] = None
                result['travel_time'] = None
            
            results.append(result)
                
        
        if sort_by == "distance" and user_coords:
            results.sort(key=lambda x: x.get('distance_km', float('inf')))
        elif sort_by == "rating":
            results.sort(key=lambda x: x.get('rating', 0), reverse=True)
        
        return results
    
    def get_directions_url(self, hospital: Dict, user_coords: Optional[Tuple[float, float]] = None) -> str:
        """
        Generate Google Maps directions URL
        """
        dest_lat = hospital.get('lat')
        dest_lon = hospital.get('lon')
        
        if not dest_lat or not dest_lon:
            # Fallback to address search
            address = f"{hospital.get('address', '')}, {hospital.get('city', '')}"
            return f"https://www.google.com/maps/search/?api=1&query={address.replace(' ', '+')}"
        
        if user_coords:
            # From user location to hospital
            return f"https://www.google.com/maps/dir/{user_coords[0]},{user_coords[1]}/{dest_lat},{dest_lon}"
        else:
            # Just hospital location
            return f"https://www.google.com/maps/search/?api=1&query={dest_lat},{dest_lon}"
    
    def get_call_url(self, phone: str) -> str:
        """Generate tel: URL for calling"""
        return f"tel:{phone.replace(' ', '')}"
    
    def get_cities_list(self) -> List[str]:
        """Get unique list of cities from hospital database"""
        cities = set()
        for hospital in self.hospitals:
            city = hospital.get('city')
            if city:
                cities.add(city)
        return sorted(list(cities))
