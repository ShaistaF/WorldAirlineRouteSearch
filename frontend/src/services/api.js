import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

const api = {
    optimizeFlight: async (origin, destination) => {
        try {
            const response = await axios.post(`${API_URL}/flights/optimize`, {
                origin,
                destination
            });
            return response.data;
        } catch (error) {
            console.error('Error optimizing flight:', error);
        }
    }
};

export default api;
