import React, { useState } from "react";
import axios from "./axiosInstance";
function App() {
  const [scores, setScores] = useState([]);

  const upload = async (resume, job_desc) => {
    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_desc", job_desc);
    const res = await axios.post("/upload", formData);
    setScores([...scores, res.data]);
  };

  return (
    <div className="App">
      {scores.map((s, idx) => (
        <div key={idx}>Score: {s.score} <progress value={s.score} max="100" /></div>
      ))}
    </div>
  );
}

