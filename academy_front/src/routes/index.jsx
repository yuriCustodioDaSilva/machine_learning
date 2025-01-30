import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "../Home";
import Predictor from "../Predictor";

const App = () => {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link> |
        <Link to="/predictor">Predictor</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/predictor" element={<Predictor />} />
      </Routes>
    </Router>
  );
};

export default App;