import React, { useEffect, useState } from "react";
import api from "./api";

function App() {
  const [devices, setDevices] = useState([]);
  const getDevices = async () => {
    const { data } = await api.service("devices").find();
    setDevices(data);
  };

  useEffect(() => {
    getDevices();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={`${process.env.PUBLIC_URL}/logo.svg`} className="App-logo" />
        {devices.map((d) => {
          return (
            <div key={d.device_id}>
              {d.device_id} - {d.occupied ? "Besetzt" : "Nicht besetzt"}
            </div>
          );
        })}
      </header>
    </div>
  );
}

export default App;
