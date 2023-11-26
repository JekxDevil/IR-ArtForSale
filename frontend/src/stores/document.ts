import { defineStore } from "pinia";
import axios from "axios";

export const useDocumentStore = defineStore({
    id: "documents",
    state: () => ({
        documents: [],
    }),
    getters: {
        hasFields: (state) => state.documents.length > 0,
    },
    actions: {
        async getDocuments(query: string) {
            try {
                const response = await axios.get(`http://localhost:8000/api/documents/get-documents/${query}/`);
                this.documents = response.data.documents;
            } catch (error) {
                console.error("Error fetching fields:", error);
                throw error;
            }
        },
    },
});
