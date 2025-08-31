import React, { useState, useEffect } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

// Styles personnalisés pour un éditeur moderne et complet
const editorStyles = `
  .rich-text-editor .ql-editor {
    min-height: 300px;
    padding: 20px;
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.6;
  }
  .rich-text-editor .ql-container {
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    border: 1px solid #e5e7eb;
  }
  .rich-text-editor .ql-toolbar {
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    border: 1px solid #e5e7eb;
    background: #f9fafb;
    padding: 12px;
  }
  .rich-text-editor .ql-toolbar .ql-formats {
    margin-right: 12px;
  }
  .rich-text-editor .ql-toolbar button {
    padding: 6px 8px;
    border-radius: 4px;
    margin: 2px;
  }
  .rich-text-editor .ql-toolbar button:hover {
    background: #e5e7eb;
  }
  .rich-text-editor .ql-toolbar button.ql-active {
    background: #6b745a;
    color: white;
  }
  .rich-text-editor .ql-color .ql-picker-options {
    padding: 8px;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  }
  .rich-text-editor .ql-color .ql-picker-item {
    border-radius: 3px;
    margin: 2px;
    width: 20px;
    height: 20px;
  }
`;

const RichTextEditor = ({ 
  value, 
  onChange, 
  placeholder = "Écrivez votre contenu...",
  height = 300,
  onSave,
  onCancel,
  saving = false,
  showButtons = true
}) => {
  const [content, setContent] = useState(value || '');

  useEffect(() => {
    setContent(value || '');
  }, [value]);

  const handleChange = (newContent) => {
    setContent(newContent);
    if (onChange) {
      onChange(newContent);
    }
  };

  // Configuration de la barre d'outils avec couleurs personnalisées
  const modules = {
    toolbar: [
      [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
      ['bold', 'italic', 'underline', 'strike'],
      [{ 'color': [
        '#000000', '#e60000', '#ff9900', '#ffff00', '#008a00', '#0066cc', '#9933ff',
        '#ffffff', '#facccc', '#ffebcc', '#ffffcc', '#cce8cc', '#cce0f5', '#ebd6ff',
        '#bbbbbb', '#f06666', '#ffc266', '#ffff66', '#66b266', '#66a3e0', '#c285ff',
        '#888888', '#a10000', '#b26b00', '#b2b200', '#006100', '#0047b2', '#6b24b2',
        '#444444', '#5c0000', '#663d00', '#666600', '#003700', '#002966', '#3d1466',
        '#6b745a', '#8a9373', '#5a6349', '#4a5339'
      ] }, { 'background': [
        '#000000', '#e60000', '#ff9900', '#ffff00', '#008a00', '#0066cc', '#9933ff',
        '#ffffff', '#facccc', '#ffebcc', '#ffffcc', '#cce8cc', '#cce0f5', '#ebd6ff',
        '#bbbbbb', '#f06666', '#ffc266', '#ffff66', '#66b266', '#66a3e0', '#c285ff',
        '#888888', '#a10000', '#b26b00', '#b2b200', '#006100', '#0047b2', '#6b24b2',
        '#444444', '#5c0000', '#663d00', '#666600', '#003700', '#002966', '#3d1466',
        '#6b745a', '#8a9373', '#5a6349', '#4a5339'
      ] }],
      [{ 'size': ['small', false, 'large', 'huge'] }],
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      [{ 'indent': '-1'}, { 'indent': '+1' }],
      [{ 'align': [] }],
      ['blockquote', 'code-block'],
      ['link', 'image'],
      ['clean']
    ],
  };

  const formats = [
    'header', 'bold', 'italic', 'underline', 'strike',
    'color', 'background', 'size', 'list', 'bullet', 'indent',
    'align', 'blockquote', 'code-block', 'link', 'image'
  ];

  return (
    <div className="rich-text-editor">
      <style>{editorStyles}</style>
      <div className="mb-6">
        <ReactQuill
          theme="snow"
          value={content}
          onChange={handleChange}
          modules={modules}
          formats={formats}
          placeholder={placeholder}
          style={{ height: `${height}px`, marginBottom: '60px' }}
          className="bg-white rounded-lg"
        />
      </div>
      
      {/* Boutons de contrôle */}
      {showButtons && (
        <div className="flex justify-end space-x-3 mt-8 pt-4 border-t border-slate-200">
          <button
            onClick={onCancel}
            className="px-6 py-3 text-gray-600 hover:bg-gray-100 rounded-xl transition-elegant font-inter"
            disabled={saving}
          >
            Annuler
          </button>
          <button
            onClick={() => onSave && onSave(content)}
            disabled={saving}
            className="px-8 py-3 gradient-sage text-white rounded-xl hover:shadow-sage transition-elegant font-inter font-medium disabled:opacity-50"
          >
            {saving ? 'Enregistrement...' : 'Enregistrer'}
          </button>
        </div>
      )}
    </div>
  );
};

export default RichTextEditor; 