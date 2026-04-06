import React, { useState, useRef } from "react";
import "./form.css";

const FORM = () => {
  const [messages] = useState([
    { role: "user", content: "chào bạn" },
    {
      role: "assistant",
      content: '{"status_code": 200, "answer": "Xin chào!..."}',
    },
  ]);

  const [files, setFiles] = useState([]);
  const inputRef = useRef();

  // Thêm file
  const handleFile = (fileList) => {
    const newFiles = Array.from(fileList);
    setFiles((prev) => [...prev, ...newFiles]);
  };

  // Xoá file
  const removeFile = (indexToRemove) => {
    setFiles((prev) => prev.filter((_, i) => i !== indexToRemove));
  };

  return (
    <div className="container">
      <div className="sidebar">
        <h2>Upload Documents</h2>

        <div
          className="dropzone"
          onClick={() => inputRef.current.click()}
          onDragOver={(e) => e.preventDefault()}
          onDrop={(e) => {
            e.preventDefault();
            handleFile(e.dataTransfer.files);
          }}
        >
          {files.length === 0 && <p>Drag & Drop hoặc click để chọn file</p>}

          {files.length > 0 && (
            <div className="file-info">
              {files.map((f, index) => (
                <div key={index} className="file-item">
                  <span>{f.name}</span>

                  <button
                    className="remove-btn"
                    onClick={(e) => {
                      e.stopPropagation();
                      removeFile(index);
                    }}
                  >
                    x
                  </button>
                </div>
              ))}
            </div>
          )}

          <input
            type="file"
            ref={inputRef}
            multiple
            hidden
            onChange={(e) => handleFile(e.target.files)}
          />
        </div>

        <button className="btn-process">Process & Add</button>
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

        <div style={{ padding: "20px" }}>
          <input
            style={{ width: "80%", padding: "10px" }}
            placeholder="Nhập câu hỏi..."
          />
        </div>
      </div>
    </div>
  );
};

export default FORM;
