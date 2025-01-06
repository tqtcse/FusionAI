import axios from 'axios';

const callGeminiAPI = async (inputData) => {
  try {
    const response = await axios.post('http://localhost:5000/gemini', inputData, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data; // Trả về kết quả từ API Gemini
  } catch (error) {
    console.error('Error calling Gemini API:', error);
    throw error;
  }
};

export default callGeminiAPI;
