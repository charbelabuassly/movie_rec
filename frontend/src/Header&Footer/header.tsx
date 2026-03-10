import { Link } from "react-router-dom";
import { ModeToggle } from "../components/mode-toggle";

export default function Header() {
    return (
        <div className="fixed top-0 w-full border-b border-border bg-background/60 text-foreground backdrop-blur-sm">
            <div className=" mx-auto max-w-3xl flex items-center justify-between px-6 py-4">
                <Link to="/" className="flex-start text-xl font-bold tracking-wide mx-3 text-foreground">
                    Logo
                </Link>

                <div className="flex items-center gap-4">
                    <Link
                        to="/login"
                        className="rounded-[20px] border border-border bg-transparent px-10 py-2 text-[14px] font-medium transition hover:bg-accent hover:text-accent-foreground "
                    >
                        Login
                    </Link>

                    <ModeToggle />
                </div>
            </div>
        </div>
    );
}