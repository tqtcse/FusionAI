import axios from 'axios';

const callLlamaAPI = async (inputData) => {
	try {
		const response = await axios.post('http://localhost:5000/llama', inputData, {
			headers: {
				'Content-Type': 'application/json'
			},
		});
		return response.data;
	} catch (error) {
		console.error('Error caling Llama API:', error);
		throw error;
	}
};

export default callLlamaAPI;