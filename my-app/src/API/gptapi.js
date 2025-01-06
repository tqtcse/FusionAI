import axios from 'axios';

const callGPTAPI = async (inputData) => {
	try {
		const response = await axios.post('http://localhost:5000/gpt', inputData, {
			headers: {
				'Content-Type': 'application/json'
			},
		});
		return response.data;
	} catch (error) {
		console.error('Error calling GPT API:', error);
		throw error;
	}
};

export default callGPTAPI;