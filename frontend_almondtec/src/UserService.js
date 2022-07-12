import axios from "axios";
import { auth } from "./LoginService";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:5002",
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: auth["token"],
  },
});

export default {
  getUser() {
    console.log("auth: ", auth);
    return apiClient.get("/user");
  },
};
