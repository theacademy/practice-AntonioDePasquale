import React from "react";

const NewContactForm = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phone, setPhone] = useState('');
    const [email, setEmail] = useState('');
    const [company, setCompany] = useState('');


    return (
        <form>
            <label>First Name:
                <input type="text" value={firstName} onChange={e => setFirstName(e.target.value)}/>
            </label>
            <label>Last Name:
                <input type="text" value={lastName} onChange={e => setLastName(e.target.value)}/>
            </label>
            <label>Phone:
                <input type="text" value={phone} onChange={e => setPhone(e.target.value)}/>
            </label>
            <label>Email:
                <input type="text" value={email} onChange={e => setEmail(e.target.value)}/>
            </label>
            <label>Company:
                <input type="text" value={company} onChange={e => setCompany(e.target.value)}/>
            </label>
        </form>
    );
};

export default NewContactForm;