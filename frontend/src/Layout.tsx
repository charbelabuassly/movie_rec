import type { ReactNode } from 'react'
import { ThemeProvider } from './components/theme-provider.js'
import Header from './Header&Footer/header.jsx'

export default function Layout({ children }: { children: ReactNode }) {
    return (
        <ThemeProvider defaultTheme="system" storageKey="vite-ui-theme">
            <Header />
            {children}
        </ThemeProvider>
    )
}