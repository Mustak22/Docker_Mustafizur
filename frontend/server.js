const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "public")));

app.get("/health", (req, res) => {
    res.json({
        status: "success",
        message: "Node.js frontend is running"
    });
});

app.post("/api/submit", async (req, res) => {
    try {
        const response = await fetch("http://backend:5000/api/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(req.body)
        });

        const data = await response.json();

        res.status(response.status).json(data);

    } catch (error) {
        console.error("Backend connection error:", error);

        res.status(500).json({
            status: "error",
            message: "Unable to connect to Flask backend"
        });
    }
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Frontend server running on port ${PORT}`);
});
