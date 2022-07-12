<script>
import { auth } from "@/LoginService.js";
export default {
  name: "Logout",
  data() {
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
