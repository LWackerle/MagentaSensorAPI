import feathers from "@feathersjs/client";
import axios from "axios";

const client = feathers();
const restClient = feathers.rest("http://80.158.52.92/api");
client.configure(restClient.axios(axios));
client.configure(feathers.authentication());

export default client;
