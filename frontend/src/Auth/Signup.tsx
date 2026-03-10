import { useState, FormEvent } from "react"
import Layout from "./Layout"
import Footer from "../Header&Footer/footer"
import { Link } from "react-router-dom";

export default function Signup() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const [errors, setErrors] = useState({
        name: "",
        email: "",
        password: "",
        confirmPassword: "",
    })

    const validate = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const newErrors = {
            name: "",
            email: "",
            password: "",
            confirmPassword: "",
        }

        {/* Name Check */ }
        if (!name.trim()) {
            newErrors.name = "Name is required"
        }
        if (name.length > 15) {
            newErrors.name = "Name must not be greater than 15 characters"
        }

        {/* Email Check */ }
        if (!email.trim()) {
            newErrors.email = "Email is required"
        }

        else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            newErrors.email = "Enter a valid email address"
        }

        {/* Password Check */ }
        if (!password.trim()) {
            newErrors.password = "Password is required"
        }
        else if (password.length < 8) {
            newErrors.password = "Password must be at least 8 characters"
        }
        else if (!/[A-Z]/.test(password)) {
            newErrors.password = "Password must contain at least 1 uppercase letter"
        }
        else if (!/[0-9]/.test(password)) {
            newErrors.password = "Password must contain at least 1 number"
        }

        {/* Confirmed Password Check */ }
        if (!confirmPassword.trim()) {
            newErrors.confirmPassword = "Please confirm your password"
        }
        else if (confirmPassword !== password) {
            newErrors.confirmPassword = "Passwords do not match"
        }

        setErrors(newErrors)

    }

    return (
        <Layout>
            <div className="h-screen bg-background text-white flex flex-col">
                <main className="flex-1 flex flex-col items-center justify-center">

                    {/* Title */}
                    <div className="w-[420px] max-w-[90vw] mt-auto">
                        <h1 className="mb-5 text-center text-[35px] text-foreground ">
                            Create Account
                        </h1>

                        {/* Email & Password */}
                        <form className="space-y-10" onSubmit={validate} noValidate autoComplete="off">

                            {/* Name */}
                            <div>
                                <label
                                    htmlFor="name"
                                    className="mb-3 block text-[14px] font-medium text-destructive"
                                >
                                    User Name
                                </label>
                                <input
                                    id="name"
                                    name="name"
                                    type="text"
                                    autoComplete="off"
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                    className={`w-full border-b border-zinc-500 bg-transparent pb-2 text-foreground outline-none transition-colors duration-500 focus:border-destructive`}
                                />

                                {errors.name && (
                                    <p className="mt-2 text-sm text-red-500">{errors.name}</p>
                                )}

                            </div>

                            {/* Email */}
                            <div>
                                <label
                                    htmlFor="email"
                                    className="mb-3 block text-[14px] font-medium text-destructive"
                                >
                                    Email Address
                                </label>
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    autoComplete="off"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    className={`w-full border-b border-zinc-500 bg-transparent pb-2 text-foreground outline-none transition-colors duration-500 focus:border-destructive`}
                                />

                                {errors.email && (
                                    <p className="mt-2 text-sm text-red-500">{errors.email}</p>
                                )}

                            </div>

                            {/* Password */}
                            <div>
                                <label
                                    htmlFor="password"
                                    className="mb-3 block text-[14px] font-medium text-destructive"
                                >
                                    Password
                                </label>
                                <input
                                    id="password"
                                    name="password"
                                    type="password"
                                    autoComplete="new-password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    className={`w-full border-b border-zinc-500 bg-transparent pb-2 text-foreground outline-none transition-colors duration-500 focus:border-destructive`}
                                />

                                {errors.password && (
                                    <p className="mt-2 text-sm text-red-500">{errors.password}</p>
                                )}

                            </div>

                            {/* ConfirmPassword */}
                            <div>
                                <label
                                    htmlFor="confirmPassword"
                                    className="mb-3 block text-[14px] font-medium text-destructive"
                                >
                                    Password
                                </label>
                                <input
                                    id="confirmPassword"
                                    name="confirmPassword"
                                    type="password"
                                    autoComplete="new-password"
                                    value={confirmPassword}
                                    onChange={(e) => setConfirmPassword(e.target.value)}
                                    className={`w-full border-b border-zinc-500 bg-transparent pb-2 text-foreground outline-none transition-colors duration-500 focus:border-destructive`}
                                />

                                {errors.confirmPassword && (
                                    <p className="mt-2 text-sm text-red-500">{errors.confirmPassword}</p>
                                )}

                            </div>

                            {/* Submit Button*/}
                            <button
                                type="submit"
                                className="mt-4 w-full rounded-full border border-zinc-600 opacity-50 py-3 text-sm font-bold text-foreground transition duration-500 hover:border-destructive hover:text-destructive cursor-pointer"
                            >
                                Create Account
                            </button>

                            <div className="flex justify-center">

                                <span className="text-foreground">
                                    Already have an account?
                                    <Link to="/login" className="ml-2 font-bold text-orange-500 transition duration-300 hover:text-foreground">
                                        LOG IN
                                    </Link>
                                </span>

                            </div>

                        </form>
                    </div>
                </main>

                <Footer />

            </div>
        </Layout>
    )
}