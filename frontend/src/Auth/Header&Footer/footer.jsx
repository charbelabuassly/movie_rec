export default function Footer() {
    return (
        <footer className="px-6 pb-8 text-xs text-foreground">
            <div className="mx-auto max-w-5xl border-b border-zinc-700 pb-5 text-center">
                <div className="flex flex-wrap items-center justify-center gap-3">
                    <span>Terms of Use</span>
                    <span>|</span>
                    <span>Privacy Policy</span>
                </div>
            </div>

            <div className="mx-auto flex max-w-5xl items-center justify-between pt-6 text-foreground">
                <span>Made By | Masked Knight, LeSalim, That-Thing</span>
                <span>ENGLISH (US)</span>
            </div>
        </footer>
    )
}