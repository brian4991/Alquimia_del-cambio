import React, { useState } from 'react';
import { Pencil, Save, X } from 'lucide-react';
import RichTextEditor from './RichTextEditor';

const EditableSection = ({ 
  sectionKey, 
  content, 
  onSave, 
  className = "",
  editClassName = "p-4 bg-yellow-50 border-2 border-yellow-300 rounded-lg",
  children 
}) => {
  const [isEditing, setIsEditing] = useState(false);
  const [saving, setSaving] = useState(false);
  
  // Extract default HTML content from children
  const getDefaultContent = () => {
    if (content) return content;
    
    // Convert React children to HTML string
    const reactElementToHTML = (element) => {
      if (typeof element === 'string') return element;
      if (typeof element === 'number') return String(element);
      if (!element) return '';
      
      if (Array.isArray(element)) {
        return element.map(reactElementToHTML).join('');
      }
      
      if (React.isValidElement(element)) {
        const { type, props } = element;
        
        // Handle text nodes
        if (!props) return '';
        
        // Get the tag name
        let tagName = typeof type === 'string' ? type : 'div';
        
        // Extract inline styles
        let styleAttr = '';
        if (props.style) {
          const styleString = Object.keys(props.style)
            .map(key => {
              const cssKey = key.replace(/([A-Z])/g, '-$1').toLowerCase();
              return `${cssKey}:${props.style[key]}`;
            })
            .join(';');
          styleAttr = ` style="${styleString}"`;
        }
        
        // Extract className
        let classAttr = props.className ? ` class="${props.className}"` : '';
        
        // Process children
        const childrenHTML = props.children ? reactElementToHTML(props.children) : '';
        
        // Self-closing tags
        if (['img', 'br', 'hr', 'input'].includes(tagName)) {
          return `<${tagName}${classAttr}${styleAttr} />`;
        }
        
        return `<${tagName}${classAttr}${styleAttr}>${childrenHTML}</${tagName}>`;
      }
      
      return '';
    };
    
    return reactElementToHTML(children);
  };
  
  const [editedContent, setEditedContent] = useState(getDefaultContent());

  const handleSave = async () => {
    setSaving(true);
    try {
      await onSave(sectionKey, editedContent);
      setIsEditing(false);
    } catch (error) {
      console.error('Error saving content:', error);
      alert('Error al guardar el contenido');
    } finally {
      setSaving(false);
    }
  };

  const handleCancel = () => {
    setEditedContent(getDefaultContent());
    setIsEditing(false);
  };
  
  const handleEdit = () => {
    // Update content from current display when starting to edit
    setEditedContent(content || getDefaultContent());
    setIsEditing(true);
  };

  if (isEditing) {
    return (
      <div className={editClassName}>
        <div className="flex justify-between items-center mb-4">
          <span className="text-sm font-semibold text-gray-700">
            Editando: {sectionKey}
          </span>
          <div className="flex space-x-2">
            <button
              onClick={handleCancel}
              disabled={saving}
              className="p-2 text-gray-600 hover:bg-gray-200 rounded-lg transition-all"
              title="Cancelar"
            >
              <X className="w-5 h-5" />
            </button>
            <button
              onClick={handleSave}
              disabled={saving}
              className="p-2 text-white bg-green-600 hover:bg-green-700 rounded-lg transition-all"
              title="Guardar"
            >
              <Save className="w-5 h-5" />
            </button>
          </div>
        </div>
        <RichTextEditor
          value={editedContent}
          onChange={setEditedContent}
          placeholder="Escribe el contenido aquí..."
          height={200}
          showButtons={false}
        />
      </div>
    );
  }

  return (
    <div className={`relative group ${className}`}>
      {/* Edit button - shows on hover */}
      <button
        onClick={handleEdit}
        className="absolute top-2 right-2 p-2 bg-blue-500 text-white rounded-lg opacity-0 group-hover:opacity-100 transition-all hover:bg-blue-600 z-10 shadow-lg"
        title="Editar contenido"
      >
        <Pencil className="w-4 h-4" />
      </button>
      
      {/* Display content or children */}
      {content ? (
        <div dangerouslySetInnerHTML={{ __html: content }} />
      ) : (
        children
      )}
    </div>
  );
};

export default EditableSection;

