interface CardProps {
    children: React.ReactNode,
    className?: string
}

export function CardBackground({ children, className }: CardProps) {
    return (
        <div className={`flex flex-col px-10 py-8 bg-(--profile-card-color) font-poppins-sans rounded-3xl shadow-xl ${className ? className: 'gap-[20px]'}`}>
            {children}
        </div>
    )
}

export function CardH1({ children }: CardProps) {
    return (
        <h1 className="font-extrabold text-[40px]">
            {children}
        </h1>
    )
}

export function CardLi({ children }: CardProps) {
    return (
        <li className="font-medium text-[32px]">
            {children}
        </li>
    )
}

export function CardP({ children }: CardProps) {
    return (
        <p className="font-medium text-[24px]">
            {children}
        </p>
    )
}

