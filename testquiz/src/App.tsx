import React from 'react';
import './App.css';import Radio from '@mui/material/Radio';
import TextField from '@mui/material/TextField';
import { useState, useEffect } from "react";

function MyButton({ title }: { title: string }) {
  
  return (
    <button>{title}</button> );
  
}
  function App() {


    const [message, setMessage] = useState('');
        //hinzugefügt
        const [ant, setAnswer] = useState('');

        useEffect(() => {
          fetch('http://localhost:5000/api/hello')
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error('Error:', error));
        }, []);

      const handleClick = async () => {
        try {
          const response = await fetch('http://localhost:5000/api/process_data', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ key:'Anwort 1'}), // Hier die Daten einfügen
          });

          const result = await response.json();
          console.log(result);

          if ('result' in result) {
            const receivedResult = result.result;
            setMessage(` ${receivedResult}`);
          } else {
            setMessage('No result found in the received data');
          }



          //Test antwort zurück
          //const answer = await response.json();
         //setAnswer(answer.answer)

          if ('answer' in result) {
            const receivedValue = result.answer;
            setAnswer(`Received value: ${receivedValue}`);

          } else {
            setAnswer('No value found in the received data');
          }







        } catch (error) {
          console.error('Error:', error);
        }
      };
  return (
    <div className="App">
      <header className="App-header">

        <p>
      
      
      <span
      style={{
        position: 'absolute',
        top: 0,
        right: 0,
        padding: '10px',
        background: 'rgba(0, 0, 0, 0,5)',
        color: 'black',
      }}
    >
      Score: <br/>    
      
      </span>
        </p>

        <span
      style={{
        position: 'absolute',
        top: 0,
        right: 120,
        padding: '10px',
        background: 'rgba(0, 0, 0, 0,5)',
        color: 'black',
      }}
    >
      Bisherige Fehler: <br/>    
      
      </span>
        <p>
          Frage 1:


        </p>
        
          <MyButton title=" Antwort 1" /> <br/>
          <MyButton title=" Antwort 2" /> <br/>
          <MyButton title=" Antwort 3" /> <br/>
          <MyButton title=" Antwort 4" /> <br/>
        
      </header>
      
    </div>
    
  
      );
    }

  


export default App;
