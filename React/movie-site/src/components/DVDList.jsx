import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ListDVDs = () => {
    const [dvds, setDvds] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get('http://dvd-library.us-east-1.elasticbeanstalk.com/dvds')
            setDvds(response.data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h1>DVD Library</h1>
            <ul>
                {dvds.map(dvd => (
                    <li key={dvd.id}>
                        {dvd.id} - {dvd.title} - {dvd.releaseYear} - {dvd.director} - {dvd.rating}
                        <button value='Details'/>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ListDVDs;