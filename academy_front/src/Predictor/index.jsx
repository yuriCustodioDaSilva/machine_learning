import { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css";

const Predictor = () => {
  const [advice, setAdvice] = useState("");

  useEffect(() => {
    const fetchAdvice = async () => {
      try {
        const response = await axios.get("https://api.adviceslip.com/advice");
        setAdvice(response.data.slip.advice);
      } catch (error) {
        console.error("Erro ao buscar advice:", error);
        setAdvice("Erro ao carregar o conselho.");
      }
    };

    fetchAdvice();
  }, []);

  return (
    <div className="container">
      <div className="box">
        <b>{advice}</b>
      </div>
    </div>
  );
};

export default Predictor;