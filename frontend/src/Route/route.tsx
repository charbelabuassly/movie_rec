import { Routes, Route } from 'react-router-dom'
import Home from '../home'
import Login from '../Auth/Login'
import ResetPassword from '../Auth/ResetPassword'
import Signup from '../Auth/Signup'

export default function Routing() {
    return (
        <Routes>
            {/* HOME PAGE */}
            <Route path="/" element={ <Home/> } />

            {/* Auth PAGES */}
            <Route path="/login" element={ <Login /> } />
            <Route path="/forgetpassword" element= { <ResetPassword /> } />
            <Route path="/createaccount" element= {<Signup />} />
        </Routes>
    )
}