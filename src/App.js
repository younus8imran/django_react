import React, { useEffect, useState } from 'react'
import "./App.css"

export default function App() {
  
  const [leads, setLeads] = useState([]);

  const fetchLeads = async() => {
      const api = await fetch('https://user-drf.herokuapp.com/api/lead/');
      const data = await api.json();
      setLeads(data);

  }

  useEffect(() => {
      fetchLeads();
  }, [])

  return (
    <div>
        {leads.map((lead) => {
            return(
                <div key={lead.id} className="card">
                    <h1>{lead.name}</h1>
                    <img src={lead.get_image} alt={lead.name} />
                    <p><strong>Email: </strong>{lead.email}</p>
                    <p><strong>Age: </strong>{lead.age}</p>
         
                </div>
            )
        })}

    </div>
  )
}
