import axios from 'axios'

const fetchData = async () => {
  try {
    const response = await axios.get('http://localhost:5000/api/data');
    return response.data;  // Trả về dữ liệu từ API
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export default fetchData;