import axios from "axios";

const FASTAPI_HOST = process.env.FASTAPI_HOST;
const FASTAPI_PORT = process.env.FASTAPI_PORT;

const baseURL = "http://0.0.0.0:8000/api/v1/";

const axiosInstance = axios.create({
  baseURL,
});

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;
