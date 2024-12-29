// src/services/api.js
const API_BASE_URL = 'http://localhost:8000/api';

// Error handler utility
const handleError = (error) => {
    console.error('API Error:', error);
    // Extract the most useful error message for the user
    const message = error.response?.data?.detail || error.message || 'An unexpected error occurred';
    throw new Error(message);
};

// API service object
export const apiService = {
    // Query endpoint
    async sendQuery(query) {
        try {
            const response = await fetch(`${API_BASE_URL}/rag/query`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data.response;
        } catch (error) {
            handleError(error);
        }
    },

    // Document upload endpoint
    async uploadDocument(file) {
        try {
            // Validate file type and size
            if (!file.type.includes('text/plain')) {
                throw new Error('Only text files are currently supported');
            }

            if (file.size > 5 * 1024 * 1024) { // 5MB limit
                throw new Error('File size must be less than 5MB');
            }

            const formData = new FormData();
            formData.append('file', file);

            const response = await fetch(`${API_BASE_URL}/rag/upload`, {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            handleError(error);
        }
    }
};