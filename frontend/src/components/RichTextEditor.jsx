import React, { useState, useEffect } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

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

  // Configuration de la barre d'outils
  const modules = {
    toolbar: [
      [{ 'header': [1, 2, 3, false] }],
      ['bold', 'italic', 'underline', 'strike'],
      [{ 'color': [] }, { 'background': [] }],
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      [{ 'indent': '-1'}, { 'indent': '+1' }],
      [{ 'align': [] }],
      ['blockquote', 'code-block'],
      ['link'],
      ['clean']
    ],
  };

  const formats = [
    'header', 'bold', 'italic', 'underline', 'strike',
    'color', 'background', 'list', 'bullet', 'indent',
    'align', 'blockquote', 'code-block', 'link'
  ];

  return (
    <div className="rich-text-editor">
      <div className="mb-4">
        <ReactQuill
          theme="snow"
          value={content}
          onChange={handleChange}
          modules={modules}
          formats={formats}
          placeholder={placeholder}
          style={{ height: `${height}px` }}
          className="bg-white rounded-lg"
        />
      </div>
      
      {/* Boutons de contrôle */}
      {showButtons && (
        <div className="flex justify-end space-x-3 mt-16">
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