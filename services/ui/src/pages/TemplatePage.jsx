import React from "react";
import AppSidebar from "../components/AppSidebar/AppSidebar";
import Header from "../components/Header/Header";

export default function TemplatePage({ children, title, icon }) {
    return (
        <div className="flex flex-col w-screen h-screen">
            <div className="flex w-full h-full">
                <div className="h-full">
                    <AppSidebar />
                </div>
                <div className="w-screen">
                    <Header title={title} icon={icon} />
                    {children}
                </div>
            </div>
            <div className="px-4 py-4 bg-slate-100 text-slate-300">
                MedTrack - 2024
            </div>
        </div>
    );
}
