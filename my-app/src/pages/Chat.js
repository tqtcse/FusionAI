import React, {useState} from 'react';
import '../css/Chat.css';
import callGeminiAPI from '../API/api'


function Chat(){

	const [messages, setMessages] = useState([]);
	const [input, setInput] = useState('');
	const [selectedModel, setSelectedModel] = useState('model1');
	const [result, setResult] = useState(null);

	const handleSend = async () => {
		// try {
		// 	const data = { input };
		// 	const response = await callGeminiAPI(data);
		// 	setResult(response);
		// } catch (error) {
		// 	console.error('Lỗi rùi:', error);
		// }
		if(input.trim() === '') return;
		setMessages([...messages, { text: input, sender: 'user' }]); // Thêm tin nhắn người dùng
	    setInput(''); // Xóa nội dung input
	    // Xử lý phản hồi giả lập (AI trả lời)
	    try {
			const response = await callGeminiAPI(input);
			setMessages((prev) => [...prev, { text:  response, sender: 'ai' }]);
		} catch (error) {
			console.error('Lỗi rùi:', error);
		}
	    // setTimeout(() => {
	    //   setMessages((prev) => [...prev, { text: 'AI trả lời: ' + input, sender: 'ai' }]);
	    // }, 1000); // Trả lời sau 1 giây
	}	

	const handleKeyDown = (e) => {
		if (e.key === 'Enter') {
			handleSend();
		}
	}

	const handleModelChange = (e) => {
    setSelectedModel(e.target.value);  // Cập nhật model khi người dùng chọn
  	};

	return (
		<div className="chat-container">
			<div className="chat-window">
				{messages.map((msg, index) => (
					<div 
					key = {index} 
					className={`messages ${msg.sender === 'user' ? 'user-message' : 'ai-message'}`}>
					{msg.text}
					</div>
					))}
			</div>
			<div className="select-model">
				 <label htmlFor="model-select"></label>
			        <select 
			          id="model-select" 
			          value={selectedModel} 
			          onChange={handleModelChange} 
			        >
			          <option value="gpt">GPT</option>
			          <option value="gemini">Gemini</option>
			          <option value="llama">Llama</option>
			        </select>
			</div>
			<div className="chat-input">
				<input type = "text" value={input} 
				onChange={(e) => setInput(e.target.value)}
				onKeyDown={handleKeyDown}
				placeholder="Nhập tin nhắn..." />
				<button onClick={handleSend}>Gửi</button>
			</div>
		</div>
		);
}

export default Chat;