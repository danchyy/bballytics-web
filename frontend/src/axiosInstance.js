import axios from 'axios';

const axiosInstance = axios.create();

axiosInstance.defaults.baseURL = "http://localhost:4000/api";

export default axiosInstance;