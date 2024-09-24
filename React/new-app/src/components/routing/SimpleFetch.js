import React, { useState, useEffect } from "react";


const FetchDataComponent = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://contactlist.us-east-1.elasticbeanstalk.com/contacts')
                if(!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const result = await response.json()
                setData(result);
                console.log(result);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }

        fetchData();

    }, [])

    if(loading) {
        return <p>Loading...</p>
    }

    if(error) {
        return <p>Error: {error.message}</p>
    }

    return (
        <div>
            <h2>Contact List Fetched Data</h2>
            <ul>
                {data.map(contact => (
                    <li key={contact.contactId}>
                        <strong>{contact.firstName} {contact.lastName}</strong><br />
                        Phone: {contact.phone}<br />
                        Email: {contact.email}<br />
                        Company: {contact.company}
                    </li>
                ))}
            </ul>
        </div>
    )
 
}

export default FetchDataComponent;
