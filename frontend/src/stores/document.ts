import { defineStore } from "pinia";
import axios from "axios";

export const useDocumentStore = defineStore({
    id: "documents",
    state: () => ({
        documents: [],
        recomandations: [],
    }),
    getters: {
        hasFields: (state) => state.documents.length > 0,
    },
    actions: {
        async getDocuments(query: string) {
            try {
                const response = await axios.get(`http://localhost:8000/api/documents/get-documents/${query}/`);
                console.log(response)
                this.documents = response.data.documents;
            } catch (error) {
                console.error("Error fetching fields:", error);
                throw error;
            }
        },
        async getRecomended(tags: array) {
            try {
                const response = await axios.get(`http://localhost:8000/api/recomandation/get-recomended/`,{params: tags});
                console.log(response)
                this.recomandations = response.data.recomandations;
            } catch (error) {
                console.error("Error fetching fields:", error);
                throw error;
            }
        },
    },
});
