<script>
import { auth } from "@/LoginService.js";
export default {
  name: "Logout",
  data() {
    auth.token = {};
    auth.authorized = false;
    console.log("logout: ", auth);
    this.$router.push({
      name: "Login",
    });
    return {
      auth,
    };
  },
};
</script>
