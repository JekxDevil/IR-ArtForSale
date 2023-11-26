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
        async getDocuments(query) {
            try {
                const response = await axios.get("/api/search/get-documents/", { params: { query } });
                this.documents = response.data.documents;
            } catch (error) {
                console.error("Error fetching fields:", error);
                throw error;
            }
        },
    },
});
