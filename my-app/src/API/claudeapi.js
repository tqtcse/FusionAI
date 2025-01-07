import axios from 'axios';

const callClaudeAPI = async (inputData) => {
	try {
		const response = await axios.post('http://localhost:5000/claude', inputData, {
			headers: {
				'Content-Type': 'application/json',
			},
		});
		return response.data;
	} catch (error) {
		console.error('Error calling Claude API:', error)
		throw error;
	}
};

export default callClaudeAPI;