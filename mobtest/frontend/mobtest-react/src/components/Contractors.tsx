import {useFetchContractorApplications} from "../api/api";

interface Props{
  user:string,
  nationality:string,
  comment:string,
  pay_rate:string
}

type userData = {
  id:number,
  nationality:string,
  user:{username:string},
  pay_rate:string,
  comment:string
} 

const ContractorsData = ({user, nationality, comment, pay_rate}:Props) => {
  return <div className="flex text-center m-8">
    <ul className="basis-1/5 border-4">
      <li>{user}</li>
      <li>100% match</li>
    </ul>
    <ul className="basis-1/5 border-4">
      <li>pay/day</li>
      <li>£300</li>
    </ul>
    <ul className="basis-1/5 border-4">
      <li>Nationality</li>
      <li>{nationality}</li>
    </ul>
    <ul className="basis-1/5 border-4">
      <li>{comment}</li>
      <li></li>
    </ul>
    <ul className="basis-1/5 border-4">
      <li>Pay rate</li>
      <li>€{pay_rate}</li>
    </ul>
  </div>
}


const Contractors = () => {
  // Return the queried Contractors here as a list

  const {data:{results} = {}} = useFetchContractorApplications()


 

  return <div className="text-center h-full w-[44rem] left-[24rem] bg-green-100 top-2 bottom-2 mx-auto absolute">

              {results ? results.map((data:userData) => {
               const {id, nationality, user:{username}, pay_rate, comment} = data
                return(
                  <ContractorsData
                  key={id}
                  user={username}
                  nationality={nationality}
                  comment={comment}
                  pay_rate={pay_rate}
                />
                )
                }): "Loading contractData ....."}
    </div>;
};

export default Contractors;
