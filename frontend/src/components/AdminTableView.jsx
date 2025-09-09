import React from 'react';

const AdminTableView = ({ tableData, tableConfig, questionText }) => {
  // Parse table data if it's a string
  let parsedData = {};
  try {
    parsedData = typeof tableData === 'string' ? JSON.parse(tableData) : tableData;
  } catch (e) {
    return (
      <div className="text-red-500 text-sm">
        ❌ Données de tableau invalides
      </div>
    );
  }

  // If no table config provided, try to infer structure from data
  let columns = tableConfig?.columns || [];
  let rows = tableConfig?.rows || 0;

  // If no config, infer from data
  if (!tableConfig && parsedData && Object.keys(parsedData).length > 0) {
    const firstRow = parsedData[Object.keys(parsedData)[0]];
    if (firstRow) {
      columns = Object.keys(firstRow).map((key, index) => ({
        title: `Colonne ${index + 1}`,
        type: 'text'
      }));
      rows = Object.keys(parsedData).length;
    }
  }

  if (!columns.length || !rows) {
    return (
      <div className="text-gray-500 text-sm">
        📊 Tableau vide ou configuration manquante
      </div>
    );
  }

  const getCellValue = (rowIndex, colIndex) => {
    return parsedData[rowIndex]?.[colIndex] || '';
  };

  const hasAnyData = () => {
    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < columns.length; col++) {
        if (getCellValue(row, col).trim()) {
          return true;
        }
      }
    }
    return false;
  };

  if (!hasAnyData()) {
    return (
      <div className="text-gray-500 text-sm">
        📊 Tableau non rempli
      </div>
    );
  }

  return (
    <div className="space-y-3">
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
        <div className="flex items-center space-x-2 mb-2">
          <span className="text-blue-700 font-medium text-sm">📊 Réponse Tableau</span>
          <span className="text-xs text-blue-600 bg-blue-100 px-2 py-1 rounded">
            {columns.length} colonnes × {rows} lignes
          </span>
        </div>
        
        <div className="overflow-x-auto">
          <table className="min-w-full border border-blue-200 rounded text-sm">
            <thead>
              <tr className="bg-blue-100">
                {columns.map((column, colIndex) => (
                  <th
                    key={colIndex}
                    className="px-3 py-2 text-left text-xs font-semibold text-blue-800 border-r border-blue-200 last:border-r-0"
                  >
                    <div className="flex items-center space-x-1">
                      <span>{column.title}</span>
                      {column.type === 'number' && (
                        <span className="text-xs text-blue-600">#</span>
                      )}
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {Array.from({ length: rows }, (_, rowIndex) => {
                // Only show rows that have at least one non-empty cell
                const hasData = columns.some((_, colIndex) => 
                  getCellValue(rowIndex, colIndex).trim()
                );
                
                if (!hasData) return null;
                
                return (
                  <tr key={rowIndex} className="border-t border-blue-200">
                    {columns.map((column, colIndex) => {
                      const value = getCellValue(rowIndex, colIndex);
                      return (
                        <td
                          key={colIndex}
                          className="px-3 py-2 border-r border-blue-200 last:border-r-0 bg-white"
                        >
                          <div className="text-gray-700">
                            {value || (
                              <span className="text-gray-400 italic">-</span>
                            )}
                          </div>
                        </td>
                      );
                    })}
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        
        <div className="mt-2 text-xs text-blue-600">
          💡 Seules les lignes avec des données sont affichées
        </div>
      </div>
    </div>
  );
};

export default AdminTableView;
