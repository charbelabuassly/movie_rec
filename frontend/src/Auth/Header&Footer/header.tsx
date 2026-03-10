import { Link } from "react-router-dom";
import { ModeToggle } from "../../components/mode-toggle";

export default function Header() {
    return (
        <div className="fixed top-0 w-full border-b border-border bg-background/60 text-foreground backdrop-blur-sm">
            <div className=" flex items-center justify-center px-6 py-4">
                <Link to="/" className="flex-start text-xl font-bold tracking-wide mx-5 text-foreground">
                    Logo
                </Link>

                {/* Eza Badak Yeha Fik Tshil Comment
                <ModeToggle />
                */}
                <ModeToggle />
            </div>
        </div>
    );
}