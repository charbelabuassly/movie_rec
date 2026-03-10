import Layout from "./Layout"
import Footer from "../Header&Footer/footer"
import { Link } from "react-router-dom";
import { useState, FormEvent } from "react"

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [errors, setErrors] = useState({
        email: "",
        password: "",
    })

    const validate = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const newErrors = {
            email: "",
            password: "",
            confirmPassword: "",
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

        setErrors(newErrors)
    }

    return (
        <Layout>
            <div className="h-screen bg-background text-white flex flex-col">
                <main className="flex-1 flex flex-col items-center justify-center">
                    <div className="w-[420px] max-w-[90vw] -mt-16">
                        <h1 className="mb-14 text-center text-5xl text-foreground font-bold">
                            Login
                        </h1>

                        <form className="space-y-10" onSubmit={validate} noValidate autoComplete="off">
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
                                    className="w-full border-b border-zinc-500 bg-transparent pb-2 text-foreground outline-none transition-colors duration-500 focus:border-destructive"
                                />
                            </div>
                            {errors.email && (
                                <p className="mt-2 text-sm text-red-500">{errors.email}</p>
                            )}

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
                                    className="w-full border-b border-zinc-500 bg-transparent pb-2 text-foreground outline-none transition-colors duration-500 focus:border-destructive"
                                />
                            </div>

                            {errors.password && (
                                <p className="mt-2 text-sm text-red-500">{errors.password}</p>
                            ) }

                            <button
                                type="submit"
                                className="mt-4 w-full rounded-full border border-zinc-600 py-3 text-sm font-bold text-foreground transition duration-500 hover:border-destructive hover:text-destructive cursor-pointer"
                            >
                                LOG IN
                            </button>

                            <div className="flex justify-center gap-3 text-sm font-bold">
                                <Link to={"/forgetpassword"}
                                    className="text-destructive transition duration-300 hover:text-chart-5 cursor-pointer"
                                    type="button"
                                >
                                    FORGOT PASSWORD?
                                </Link>

                                <span className="text-foreground">|</span>

                                <Link to={"/createaccount"}
                                    className="text-destructive transition duration-300 hover:text-chart-5 cursor-pointer"
                                    type="button"
                                >
                                    CREATE ACCOUNT
                                </Link>

                            </div>
                        </form>
                    </div>
                </main>

                <Footer />

            </div>
        </Layout>
    )
}