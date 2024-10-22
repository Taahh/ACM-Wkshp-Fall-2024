'use client'
import { useState } from 'react';

export default function TodoList() {
  const [todos, setTodos] = useState<string[]>([]);
  const [newTodo, setNewTodo] = useState('');

  // Function to add a new todo item
  const addTodo = () => {
    if (newTodo.trim() !== '') {
      setTodos([...todos, newTodo.trim()]);
      setNewTodo('');
    }
  };

  // Function to remove a todo item by index
  const removeTodo = (index: number) => {
    setTodos(todos.filter((_, i) => i !== index));
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-50">
      <div className="w-full max-w-md p-4 bg-white rounded shadow">
        <h1 className="text-2xl font-bold text-gray-800 mb-4 text-center">
          To-do List
        </h1>
        <div className="flex mb-4">
          <input
            type="text"
            className="flex-grow px-3 py-2 mr-2 border rounded text-gray-800"
            placeholder="Add a new task"
            value={newTodo}
            onChange={(e) => setNewTodo(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter') {
                addTodo();
              }
            }}
          />
          <button
            onClick={addTodo}
            className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Add
          </button>
        </div>
        <ul className="space-y-2">
          {todos.map((todo, index) => (
            <li
              key={index}
              className="flex justify-between items-center px-3 py-2 bg-gray-100 rounded text-gray-800"
            >
              <span>{todo}</span>
              <button
                onClick={() => removeTodo(index)}
                className="text-red-500 hover:text-red-700"
              >
                &times;
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}