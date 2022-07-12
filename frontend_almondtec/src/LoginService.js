import { reactive } from "vue";
import router from "./router";

export const auth = reactive({
  token: {},
  authorized: false,
  async login(email, password) {
    const url = "http://127.0.0.1:5002/login";
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        email: email,
        password: password,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    console.log("response: ", response);
    const data = await response.json();
    console.log("data: ", data);
    if (data["success"]) {
      this.token = data["token"];
      localStorage.setItem("token", data["token"]);
      this.authorized = true;
      router.push({
        name: "User",
      });
    } else {
      this.displayNotification(data["message"], "danger");
    }
  },
  displayNotification(message, category) {
    this.showNotification = true;
    this.notificationMessage = message;
    this.notificationCategory = category;
  },
  showNotification: false,
  notificationMessage: "",
  notificationCategory: "",
});
