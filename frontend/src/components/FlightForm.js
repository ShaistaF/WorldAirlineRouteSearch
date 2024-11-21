import React, { useState } from 'react';
import api from '../services/api';

function FlightForm() {
    const [origin, setOrigin] = useState('');
    const [destination, setDestination] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await api.optimizeFlight(origin, destination);
        console.log(response);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input 
                type="text" 
                value={origin} 
                onChange={(e) => setOrigin(e.target.value)} 
                placeholder="Origin" 
            />
            <input 
                type="text" 
                value={destination} 
                onChange={(e) => setDestination(e.target.value)} 
                placeholder="Destination" 
            />
            <button type="submit">Plan Flight</button>
        </form>
    );
}

export default FlightForm;
