import Layout from "./Layout"
import Footer from "../Header&Footer/footer"
import { Link } from "react-router-dom";
import { useState, FormEvent } from "react"

export default function ResetPassword() {
    const [email, setEmail] = useState("");

    const [errors, setErrors] = useState({
        email: "",
    })

    const validate = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const newErrors = {
            name: "",
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

        setErrors(newErrors)
    }
    return (
        <Layout>
            <div className="h-screen bg-background text-white flex flex-col">
                <main className="flex-1 flex flex-col items-center justify-center">
                    <div className="w-[420px] max-w-[90vw] -mt-16">
                        <h1 className="mb-14 mt-15 text-center text-4xl text-foreground ">
                            Reset Password
                        </h1>

                        <div>
                            <h2 className="mb-5 text-zinc-500 text-center ">
                                A link will be sent to your email address in-order to reset your password.
                            </h2>
                        </div>

                        <form className="space-y-10" onSubmit={validate} noValidate autoComplete="off">

                             {/* Email */ }
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

                            <button
                                type="submit"
                                className="mt-4 w-full rounded-full border border-zinc-600 py-3 text-[14px] font-bold text-foreground transition duration-500 hover:border-destructive opacity-50 hover:text-destructive cursor-pointer"
                            >
                                Send
                            </button>


                        </form>
                    </div>
                </main>

                <Footer />

            </div>
        </Layout>
    )
}