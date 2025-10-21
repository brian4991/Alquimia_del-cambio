import React, { useState, useEffect } from 'react';

const ExerciseTable = ({ 
  tableConfig, 
  questionIndex, 
  cardId, 
  initialData = {}, 
  onDataChange, 
  readOnly = false 
}) => {
  const [tableData, setTableData] = useState({});

  // Initialize table data
  useEffect(() => {
    if (initialData && Object.keys(initialData).length > 0) {
      setTableData(initialData);
    } else {
      // Initialize empty table
      const emptyData = {};
      for (let row = 0; row < tableConfig.rows; row++) {
        emptyData[row] = {};
        tableConfig.columns.forEach((col, colIndex) => {
          emptyData[row][colIndex] = '';
        });
      }
      setTableData(emptyData);
    }
  }, [initialData, tableConfig]);

  const handleCellChange = (rowIndex, colIndex, value) => {
    if (readOnly) return;
    
    const newData = {
      ...tableData,
      [rowIndex]: {
        ...tableData[rowIndex],
        [colIndex]: value
      }
    };
    
    setTableData(newData);
    
    // Notify parent component
    if (onDataChange) {
      onDataChange(newData);
    }
  };

  const getCellValue = (rowIndex, colIndex) => {
    return tableData[rowIndex]?.[colIndex] || '';
  };

  const renderCell = (rowIndex, colIndex, column) => {
    const value = getCellValue(rowIndex, colIndex);
    const cellId = `table-${cardId}-${questionIndex}-${rowIndex}-${colIndex}`;

    if (readOnly) {
      return (
        <div className="px-3 py-2 text-sm text-gray-700 bg-gray-50">
          {value || '-'}
        </div>
      );
    }

    if (column.type === 'number') {
      return (
        <input
          id={cellId}
          type="number"
          value={value}
          onChange={(e) => handleCellChange(rowIndex, colIndex, e.target.value)}
          className="w-full px-3 py-2 text-sm border-0 focus:ring-1 focus:ring-orange-500 focus:outline-none"
          placeholder="0"
          min={column.min || undefined}
          max={column.max || undefined}
        />
      );
    }

    return (
      <input
        id={cellId}
        type="text"
        value={value}
        onChange={(e) => handleCellChange(rowIndex, colIndex, e.target.value)}
        className="w-full px-3 py-2 text-sm border-0 focus:ring-1 focus:ring-orange-500 focus:outline-none"
        placeholder="..."
      />
    );
  };

  if (!tableConfig || !tableConfig.columns) {
    return <div className="text-red-500">Configuration de tableau invalide</div>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full border border-orange-200 rounded-lg overflow-hidden">
        <thead>
          <tr className="bg-orange-100">
            {tableConfig.columns.map((column, colIndex) => (
              <th
                key={colIndex}
                className="px-3 py-3 text-left text-sm font-semibold text-orange-800 border-r border-orange-200 last:border-r-0"
              >
                <div className="flex items-center space-x-2">
                  <span>{column.title}</span>
                  {column.type === 'number' && (
                    <span className="text-xs text-orange-600 bg-orange-200 px-1 rounded">
                      #
                    </span>
                  )}
                </div>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {Array.from({ length: tableConfig.rows }, (_, rowIndex) => (
            <tr key={rowIndex} className="border-t border-orange-200">
              {tableConfig.columns.map((column, colIndex) => (
                <td
                  key={colIndex}
                  className="border-r border-orange-200 last:border-r-0 bg-white"
                >
                  {renderCell(rowIndex, colIndex, column)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ExerciseTable;
