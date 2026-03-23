import React, { useState } from 'react';
import { Send, Upload, FileText, X, Plus } from 'lucide-react';
import './Form.css'; // Quan trọng: Import file CSS vừa tạo

const FORM = () => {
  const [messages] = useState([
    { role: 'user', content: 'chào bạn' },
    { role: 'assistant', content: '{"status_code": 200, "answer": "Xin chào!..."}' }
  ]);

  return (
    <div className="container">
      {/* Sidebar */}
      <div className="sidebar">
        <h2>Upload Documents</h2>
        <div className="dropzone">
          <p>Drag and drop file here</p>
          <button>Browse files</button>
        </div>
        <button className="btn-process">Process & Add</button>
        
        <div style={{flex: 1}}>
          <h3>Documents</h3>
          <p>2 document(s) in knowledge base</p>
          {/* List docs... */}
        </div>
      </div>

      {/* Chat Area */}
      <div className="chat-area">
        <div className="messages">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              <div className="bubble">{msg.content}</div>
            </div>
          ))}
        </div>
        
        <div style={{padding: '20px'}}>
           <input style={{width: '80%', padding: '10px'}} placeholder="Nhập câu hỏi..." />
        </div>
      </div>
    </div>
  );
};

export default FORM;