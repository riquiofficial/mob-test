import Contractors from './Contractors';
import { useState } from 'react';


interface props {
  modalHandler: () => void
  modalState:boolean
}




const ModalButton = ({modalHandler, modalState}:props) => {
  // This button should open a modal displaying contractor data

  const switchModalState = () => {
    modalHandler()
  }
  
  return <>
          <button className="bg-green-100 p-2 rounded-sm" onClick={switchModalState}>{modalState ? 'Close Modal' : "Open Modal"}</button>
        </>;
};




const Modal = () => {
  const [openModal, setOpenModal] = useState<boolean>(false)



  return <div className="h-screen relative">
      {openModal && <Contractors/>}
      <ModalButton modalHandler={() => setOpenModal(prev => !prev)} modalState={openModal}/>
  </div>

}


export default Modal



