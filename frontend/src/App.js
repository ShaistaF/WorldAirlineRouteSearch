import React from 'react';
import FlightForm from './components/FlightForm';
import FlightResults from './components/FlightResults';

function App() {
    return (
        <div>
            <h1>AeroPath</h1>
            <FlightForm />
            <FlightResults />
        </div>
    );
}

export default App;
