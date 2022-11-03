import { useQuery } from "react-query";
import { KEY_FETCH_CONTRACTORS } from "../constants";
import axios from "axios";


export const ROOT = "http://localhost:8000";

const endPoints = {
  contractors:"/api/testapp/contract/"
}


export const useFetchContractorApplications = () => {
  
  return  useQuery(
      KEY_FETCH_CONTRACTORS,
      async () => {
        const url = ROOT + endPoints.contractors;
        const { data } = await axios.get(url);
        return data;
      },
    );

  };